# AI Chat Assistant

A modern, interactive AI chat assistant built with Streamlit and powered by Google's Gemini AI. This project features a complete development environment with modern Python tooling, comprehensive configuration management, and professional development practices.

## 🚀 Features

- 🤖 **AI-Powered Conversations**: Leverages Google's Gemini 2.0 Flash model for intelligent responses
- 💬 **Interactive Chat Interface**: Clean, user-friendly chat interface built with Streamlit
- 🧠 **Smart Query Handling**: Special responses for common queries about the creator and assistant identity
- 📱 **Responsive Design**: Works seamlessly across different devices and screen sizes
- 🔄 **Session Management**: Maintains chat history throughout the session
- 🗑️ **Clear Chat**: Easy option to reset conversation history
- 🛡️ **Security**: Environment-based API key management
- 🛠️ **Development Tools**: Complete IDE setup with linting, formatting, and testing
- 📦 **Modern Python**: pyproject.toml configuration with dependency management

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key
- Git (for version control)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai-chat-assistant
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using uv (modern Python package manager)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or using uv (recommended)
uv pip install -r requirements.txt
```

### 4. Set Up Google AI API Key
**Option A: Environment Variable (Recommended)**
```bash
export GOOGLE_API_KEY="your-actual-api-key-here"
```

**Option B: Streamlit Secrets (for Streamlit Cloud)**
Create a `.streamlit/secrets.toml` file:
```toml
GOOGLE_API_KEY = "your-actual-api-key-here"
```

**Option C: Direct Configuration**
Replace the API key in `app.py` (not recommended for production):
```python
API_KEY = "your-actual-api-key-here"
```

## 🎯 Usage

### Running the Application
```bash
# Basic usage
streamlit run app.py

# Development mode
streamlit run app.py --server.headless true

# Custom port
streamlit run app.py --server.port 8502
```

### Accessing the Application
- Open your browser and navigate to `http://localhost:8501`
- Start chatting with the AI assistant!

## 📁 Project Structure

```
ai-chat-assistant/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── pyproject.toml           # Modern Python project configuration
├── uv.lock                  # Dependency lock file
├── README.md                # Project documentation
├── REPORT.md                # Technical report
├── CONTRIBUTING.md          # Contribution guidelines
├── CHANGELOG.md             # Version history
├── LICENSE                  # License information
├── .gitignore              # Git ignore patterns
├── .vscode/                # VSCode configuration
│   ├── settings.json       # Editor settings
│   ├── extensions.json     # Recommended extensions
│   ├── launch.json         # Debug configurations
│   └── tasks.json          # Build tasks
└── .gitlab/                # GitLab templates
    └── issue_templates/    # Issue and MR templates
```

## ⚙️ Configuration

### Development Environment
The project includes comprehensive VSCode configuration for optimal development experience:

- **Code Formatting**: Black formatter with isort import sorting
- **Linting**: Flake8, mypy, and Ruff for code quality
- **Testing**: Pytest configuration with coverage reporting
- **Debugging**: Launch configurations for Streamlit and Python
- **Tasks**: Automated build, test, and formatting tasks

### API Key Setup
**⚠️ Security Note**: Never commit API keys to version control. Use environment variables or secure secret management for production deployments.

## 🎮 Special Commands

The assistant recognizes and responds to special queries:
- "Who are you?" / "What is your name?"
- "Your creator" / "Rakesh"
- "Nova"

## 🔧 Development

### Available Commands
```bash
# Run the application
streamlit run app.py

# Run tests
python -m pytest

# Format code
python -m black .

# Sort imports
python -m isort .

# Type checking
python -m mypy .

# Lint code
python -m flake8 .
```

### VSCode Integration
- Press `F5` to debug the application
- Use `Ctrl+Shift+P` → "Tasks: Run Task" for build tasks
- Install recommended extensions for full development experience

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your Google AI API key is valid and has sufficient quota
   - Check that the API key is properly configured (environment variable or secrets)

2. **Import Errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+
   - Try recreating virtual environment

3. **Streamlit Issues**
   - Make sure port 8501 is available
   - Check firewall settings
   - Try: `streamlit run app.py --server.port 8502`

4. **Development Tools Issues**
   - Install recommended VSCode extensions
   - Ensure Python interpreter is properly configured
   - Check VSCode settings are loaded

## 🤝 Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created by Rakesh

---

**Note**: This application requires an active internet connection to communicate with Google's Gemini API.

**Development Status**: 🚧 Active development with modern Python tooling and comprehensive configuration management.
