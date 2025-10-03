# Contributing to AI Chat Assistant

Thank you for your interest in contributing to the AI Chat Assistant project! This document provides guidelines for contributing to the codebase.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git and GitHub account
- Familiarity with Python and Streamlit
- Google AI API key (for testing)

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://code.swecha.org/RakeshGajula
   ai-chat-assistant
   git
   cd ai-chat-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Set up environment variables**
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```

5. **Run the development server**
   ```bash
   streamlit run app.py
   ```

## Development Process

### Branch Naming Convention

Use descriptive branch names following this pattern:
- `feature/feature-name` - for new features
- `bugfix/bug-description` - for bug fixes
- `hotfix/critical-issue` - for critical fixes
- `docs/documentation-update` - for documentation changes

### Commit Message Guidelines

Follow the [Conventional Commits](https://conventionalcommits.org/) specification:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat: add user authentication system
fix: resolve API key validation error
docs: update installation instructions
```

## Pull Request Process

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow coding standards
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Run tests
   python -m pytest

   # Run linting
   flake8 app.py

   # Test the application
   streamlit run app.py
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add user authentication system"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to the original repository
   - Click "Compare & pull request"
   - Provide a clear title and description
   - Reference any related issues

### Pull Request Template

```markdown
## Description

Briefly describe the changes made in this PR.

## Related Issues

- Closes #123
- Related to #456

## Changes Made

- Added new feature X
- Fixed bug Y
- Updated documentation Z

## Testing

- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] All tests pass

## Screenshots (if applicable)

Add screenshots of UI changes or new features.

## Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added for new functionality
- [ ] Documentation updated
- [ ] PR title follows conventional commit format
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) guidelines
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter)
- Use descriptive variable and function names

### Code Organization

```
app.py                    # Main application file
src/
├── components/          # Reusable UI components
├── utils/              # Utility functions
├── models/             # Data models
└── tests/              # Test files
```

### Best Practices

1. **Error Handling**
   ```python
   try:
       # Your code here
       pass
   except SpecificException as e:
       # Handle specific errors
       pass
   except Exception as e:
       # Handle general errors
       pass
   ```

2. **Type Hints**
   ```python
   from typing import List, Dict, Optional

   def process_message(message: str) -> Optional[str]:
       # Function implementation
       pass
   ```

3. **Docstrings**
   ```python
   def function_name(param1: str, param2: int) -> bool:
       """
       Brief description of what the function does.

       Args:
           param1: Description of param1
           param2: Description of param2

       Returns:
           Description of return value

       Raises:
           SpecificException: When specific error occurs
       """
       pass
   ```

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_chat.py

# Run with coverage
python -m pytest --cov=src

# Run with verbose output
python -m pytest -v
```

### Writing Tests

```python
import pytest
from app import handle_special_queries

def test_special_queries():
    """Test special query handling."""
    assert handle_special_queries("Who are you?") == "I am AI CHAT ASSISTANT, created by Rakesh."
    assert handle_special_queries("Tell me about your creator") == "Rakesh, the creator of AI CHAT ASSISTANT, is passionate about tech and AI."
    assert handle_special_queries("Regular question") is None
```

### Test Coverage

Aim for at least 80% code coverage for new features.

## Documentation

### Documentation Standards

- Use clear, concise language
- Include examples where applicable
- Keep documentation up-to-date with code changes
- Use proper markdown formatting

### Documentation Files

- `README.md`: Project overview and setup instructions
- `CONTRIBUTING.md`: This file
- `CHANGELOG.md`: Version history
- `REPORT.md`: Technical documentation
- Inline code documentation (docstrings)

### Updating Documentation

When making changes that affect user-facing functionality:

1. Update relevant documentation files
2. Add examples if introducing new features
3. Update screenshots if UI changes are made
4. Ensure all installation and setup instructions remain accurate

## Community

### Getting Help

- Create an issue for bug reports or feature requests
- Join discussions in the Issues section
- Follow the project on GitHub for updates

### Reporting Bugs

When reporting bugs, please include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment information (Python version, OS, etc.)
- Screenshots (if applicable)

### Suggesting Features

Feature requests should include:

- Clear description of the proposed feature
- Use case and benefits
- Potential implementation approach
- Any alternatives considered

## Acknowledgments

Thank you for contributing to the AI Chat Assistant project! Your contributions help improve the application for everyone.

---

**Last Updated**: December 2024
**Version**: 1.0.0
