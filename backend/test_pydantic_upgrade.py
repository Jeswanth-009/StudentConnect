#!/usr/bin/env python3
"""
Test script to verify Pydantic v2 compatibility
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    # Test basic imports
    from models.schemas import (
        UserCreate, UserResponse, PostCreate, PostResponse, 
        CommentCreate, CommentResponse, Token
    )
    from datetime import datetime
    
    print("✅ All schema imports successful")
    
    # Test basic model creation
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "name": "Test User",
        "password": "testpass123"
    }
    
    user_create = UserCreate(**user_data)
    print(f"✅ UserCreate model works: {user_create.email}")
    
    # Test model_dump (Pydantic v2 method)
    user_dict = user_create.model_dump()
    print(f"✅ model_dump() works: {type(user_dict)}")
    
    # Test CommentResponse with self-reference
    comment_data = {
        "id": "123",
        "post_id": "456",
        "author_id": "789",
        "author_name": "Test Author",
        "author_username": "testauthor",
        "content": "Test comment",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "replies": []
    }
    
    comment = CommentResponse(**comment_data)
    print(f"✅ CommentResponse with self-reference works: {comment.content}")
    
    print("🎉 All Pydantic v2 compatibility tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
