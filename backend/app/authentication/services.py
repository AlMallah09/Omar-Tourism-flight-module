from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.users.models import User
from app.authentication.utils import (verify_password,hash_password,)
from app.admin.services import create_audit_log
from app.authentication.models import PasswordHistory

import secrets
from app.authentication.models import PasswordResetToken


def validate_password_strength(password: str):
    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long."
        )

    if not any(char.isupper() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter."
        )

    if not any(char.islower() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one lowercase letter."
        )

    if not any(char.isdigit() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one number."
        )

def change_password(
    db: Session,
    user: User,
    current_password: str,
    new_password: str,
):
    if not verify_password(current_password, user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="Current password is incorrect."
        )
    
    if verify_password(new_password, user.password_hash):
        raise HTTPException(
           status_code=400,
           detail="New password must be different from the current password."
    )

    if len(new_password) < 8:
        raise HTTPException(
           status_code=400,
           detail="Password must be at least 8 characters long."
    )

    validate_password_strength(new_password)

    password_history = (
    db.query(PasswordHistory)
    .filter(PasswordHistory.user_id == user.user_id)
    .order_by(PasswordHistory.created_at.desc())
    .limit(5)
    .all()
)

    for old_password in password_history:
        if verify_password(new_password, old_password.password_hash):
            raise HTTPException(
                status_code=400,
                detail="You cannot reuse a previously used password."
        )
    
    history = PasswordHistory(
    user_id=user.user_id,
    password_hash=user.password_hash
)

    db.add(history)

    user.password_hash = hash_password(new_password)
    user.password_changed_at = datetime.utcnow()
    user.must_change_password = False
    user.failed_login_attempts = 0


    db.commit()
    db.refresh(user)


    create_audit_log(
        db=db,
        admin_id=user.user_id,
        action="CHANGE_PASSWORD",
        target_type="User",
        target_id=user.user_id,
        description="Password changed successfully."
    )

    return {"message": "Password changed successfully."}

def forgot_password(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {
            "message": "If an account with this email exists, a password reset link has been generated.",
            "reset_token": None
        }
    
    db.query(PasswordResetToken).filter(
    PasswordResetToken.user_id == user.user_id,
    PasswordResetToken.used == False
    ).update(
    {
        PasswordResetToken.used: True
    },
    synchronize_session=False
)

    token = secrets.token_urlsafe(32)

    reset_token = PasswordResetToken(
        user_id=user.user_id,
        token=token,
        expires_at=datetime.utcnow() + timedelta(minutes=30),
        used=False
    )

    db.add(reset_token)
    db.commit()

    return {
        "message": "If an account with this email exists, a password reset link has been generated.",
        "reset_token": token
    }

def reset_password(db: Session, token: str, new_password: str):
    reset_token = db.query(PasswordResetToken).filter(
        PasswordResetToken.token == token,
        PasswordResetToken.used == False
    ).first()

    if not reset_token:
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired reset token."
        )

    if reset_token.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired reset token."
        )

    user = db.query(User).filter(
        User.user_id == reset_token.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    validate_password_strength(new_password)

    if verify_password(new_password, user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="You cannot reuse a previously used password."
        )

    password_history = (
        db.query(PasswordHistory)
        .filter(PasswordHistory.user_id == user.user_id)
        .order_by(PasswordHistory.changed_at.desc())
        .limit(5)
        .all()
    )

    for old_password in password_history:
        if verify_password(new_password, old_password.password_hash):
            raise HTTPException(
                status_code=400,
                detail="You cannot reuse a previously used password."
            )

    history = PasswordHistory(
        user_id=user.user_id,
        password_hash=user.password_hash
    )

    db.add(history)

    user.password_hash = hash_password(new_password)
    user.password_changed_at = datetime.utcnow()
    user.must_change_password = False
    user.failed_login_attempts = 0
    user.account_locked = False

    reset_token.used = True

    db.commit()
    db.refresh(user)

    create_audit_log(
        db=db,
        admin_id=user.user_id,
        action="RESET_PASSWORD",
        target_type="User",
        target_id=user.user_id,
        description="Password reset using reset token."
    )

    return {"message": "Password reset successfully."}

def cleanup_expired_reset_tokens(db: Session):
    db.query(PasswordResetToken).filter(
        PasswordResetToken.expires_at < datetime.utcnow()
    ).delete(synchronize_session=False)

    db.commit()

    return {"message": "Expired password reset tokens cleaned successfully."}