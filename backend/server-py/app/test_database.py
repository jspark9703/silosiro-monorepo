#!/usr/bin/env python3
"""
Database test script for silosiro application
Run this script to test database connection and table creation
"""

import os
import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from src.db.db import initialize_database, test_db_connection, create_tables, get_session
from sqlalchemy import text

def main():
    """Main test function"""
    print("=" * 50)
    print("Silosiro Database Test")
    print("=" * 50)
    
    # Set default environment variables if not set
    os.environ.setdefault('DB_HOST', 'localhost')
    os.environ.setdefault('DB_PORT', '5432')
    os.environ.setdefault('DB_NAME', 'silosiro_db')
    os.environ.setdefault('DB_USER', 'postgres')
    os.environ.setdefault('DB_PASSWORD', 'password')
    
    print(f"Database Configuration:")
    print(f"  Host: {os.environ['DB_HOST']}")
    print(f"  Port: {os.environ['DB_PORT']}")
    print(f"  Database: {os.environ['DB_NAME']}")
    print(f"  User: {os.environ['DB_USER']}")
    print()
    
    try:
        # Test database connection
        print("1. Testing database connection...")
        if test_db_connection():
            print("   ✓ Database connection successful")
        else:
            print("   ✗ Database connection failed")
            return False
        
        # Create tables
        print("\n2. Creating database tables...")
        if create_tables():
            print("   ✓ Database tables created successfully")
        else:
            print("   ✗ Failed to create database tables")
            return False
        
        # List created tables
        print("\n3. Listing created tables...")
        try:
            with get_session() as session:
                result = session.execute(text("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                    ORDER BY table_name
                """))
                tables = [row[0] for row in result.fetchall()]
                if tables:
                    print("   Created tables:")
                    for table in tables:
                        print(f"     - {table}")
                else:
                    print("   No tables found")
        except Exception as e:
            print(f"   ✗ Error listing tables: {e}")
        
        # Test User table structure
        print("\n4. Testing User table structure...")
        try:
            with get_session() as session:
                result = session.execute(text("""
                    SELECT column_name, data_type, is_nullable
                    FROM information_schema.columns
                    WHERE table_name = 'users'
                    ORDER BY ordinal_position
                """))
                columns = result.fetchall()
                if columns:
                    print("   User table columns:")
                    for col in columns:
                        nullable = "NULL" if col[2] == "YES" else "NOT NULL"
                        print(f"     - {col[0]}: {col[1]} ({nullable})")
                else:
                    print("   User table not found")
        except Exception as e:
            print(f"   ✗ Error checking User table: {e}")
        
        print("\n" + "=" * 50)
        print("Database test completed successfully!")
        print("=" * 50)
        return True
        
    except Exception as e:
        print(f"\n✗ Database test failed with error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
