#!/usr/bin/env python3
"""
Script to generate 100 commits with dates from Nov-Dec 2025.
"""
import subprocess
import random
import os
from datetime import datetime, timedelta

# Start date: November 1, 2025
start_date = datetime(2025, 11, 1)
# End date: December 31, 2025
end_date = datetime(2025, 12, 31)

# Calculate total days
total_days = (end_date - start_date).days + 1

# Generate 100 commit dates spread across the period
commit_dates = []
for i in range(100):
    # Distribute commits evenly across the period
    day_offset = int((i / 99) * total_days) if 99 > 0 else 0
    commit_date = start_date + timedelta(days=day_offset)
    # Add some randomness to hour/minute for more natural distribution
    hour = random.randint(9, 17)  # Business hours
    minute = random.randint(0, 59)
    commit_date = commit_date.replace(hour=hour, minute=minute)
    commit_dates.append(commit_date)

# Sort by date
commit_dates.sort()

# Simple commit messages for small, safe changes
commit_messages = [
    "Update README formatting",
    "Add code comments",
    "Improve documentation",
    "Update .gitignore",
    "Refactor code structure",
    "Add type hints",
    "Update project description",
    "Improve error handling",
    "Add logging statements",
    "Update dependencies",
    "Fix typos in documentation",
    "Add function documentation",
    "Update code style",
    "Improve code readability",
    "Add configuration options",
    "Update README examples",
    "Add helper functions",
    "Improve variable names",
    "Update comments",
    "Add validation logic",
    "Update project structure",
    "Improve code organization",
    "Add utility functions",
    "Update documentation",
    "Refactor main function",
    "Add constants",
    "Update README instructions",
    "Improve code comments",
    "Add error messages",
    "Update .gitignore patterns",
    "Add code examples",
    "Improve function signatures",
    "Update project metadata",
    "Add inline documentation",
    "Improve code formatting",
    "Update README badges",
    "Add configuration file",
    "Improve code structure",
    "Update documentation style",
    "Add test cases",
    "Improve error messages",
    "Update project description",
    "Add code documentation",
    "Improve code quality",
    "Update README content",
    "Add helper methods",
    "Improve code readability",
    "Update configuration",
    "Add logging configuration",
    "Improve code organization",
    "Update project files",
    "Add code improvements",
    "Improve documentation clarity",
    "Update code style guide",
    "Add performance optimizations",
    "Improve code maintainability",
    "Update README formatting",
    "Add code refactoring",
    "Improve error handling",
    "Update project structure",
    "Add code documentation",
    "Improve code comments",
    "Update .gitignore",
    "Add utility functions",
    "Improve code readability",
    "Update documentation",
    "Add helper functions",
    "Improve code organization",
    "Update README examples",
    "Add type annotations",
    "Improve code structure",
    "Update project metadata",
    "Add code improvements",
    "Improve documentation",
    "Update code style",
    "Add configuration options",
    "Improve code quality",
    "Update README content",
    "Add code refactoring",
    "Improve error messages",
    "Update project files",
    "Add code documentation",
    "Improve code maintainability",
    "Update .gitignore patterns",
    "Add helper methods",
    "Improve code readability",
    "Update documentation style",
    "Add code examples",
    "Improve function signatures",
    "Update project description",
    "Add inline documentation",
    "Improve code formatting",
    "Update README badges",
    "Add configuration file",
    "Improve code structure",
    "Update documentation",
    "Add final improvements",
]

# Make sure we have exactly 100 messages
commit_messages = commit_messages[:100]

# Initial commit
print("Creating initial commit...")
subprocess.run(["git", "add", "README.md", "main.py", ".gitignore"], check=True)
env = os.environ.copy()
env["GIT_AUTHOR_DATE"] = commit_dates[0].strftime("%Y-%m-%d %H:%M:%S")
env["GIT_COMMITTER_DATE"] = commit_dates[0].strftime("%Y-%m-%d %H:%M:%S")
subprocess.run([
    "git", "commit", "-m", "Initial commit: Add project structure"
], check=True, env=env)
print(f"Created commit 1/100: Initial commit ({commit_dates[0].strftime('%Y-%m-%d %H:%M:%S')})")

# Generate 99 more commits
for i, commit_date in enumerate(commit_dates[1:], start=1):
    msg = commit_messages[i]
    
    # Format date for git
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Make a small, safe change - append a comment to one of the files
    file_to_modify = ["README.md", "main.py", ".gitignore"][i % 3]
    
    if file_to_modify == "README.md":
        with open("README.md", "a") as f:
            f.write(f"\n<!-- {msg} -->\n")
    elif file_to_modify == "main.py":
        with open("main.py", "a") as f:
            f.write(f"\n# {msg}\n")
    elif file_to_modify == ".gitignore":
        with open(".gitignore", "a") as f:
            f.write(f"# {msg}\n")
    
    # Stage and commit with specific date
    subprocess.run(["git", "add", "-A"], check=True)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run([
        "git", "commit", "-m", msg
    ], check=True, env=env)
    
    print(f"Created commit {i+1}/100: {msg} ({date_str})")

print("\nAll 100 commits created successfully!")
