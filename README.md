# Instagram Automation Agent - Hackathon Project

An intelligent automation system for Instagram using Droidrun and Google Gemini AI. This project provides two specialized agents to automate Instagram interactions, saving precious time for the user while they can indulge in other productive activities.

## Contributors

<a href="https://github.com/DSK-champ/AI-Instagram-Agent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=DSK-champ/AI-Instagram-Agent" />
</a>


## 🤖 Agents

### 1. Reel Reactor
Automatically reacts to unread reels in Instagram Direct Messages. The agent:
- Opens Instagram and navigates to Direct Messages
- Identifies unread chats with blue dot indicators
- Analyzes reel content (caption, comments, any readable entities)
- Reacts with appropriate emojis based on content sentiment

### 2. Feed Customiser
Customizes the user's Instagram explore feed by training it with their interests. The agent:
- Takes user preferences as input (e.g., "Educational, Funny, Marvel edits")
- Searches for relevant content in Instagram Explore
- Likes 10 continuous posts/reels per interest category
- Helps train the algorithm to show more of what they would want to see

## Technologies
- python
- droidrun
   The main component of our project that controls the actions on the phone

## Basic Working
- Using the Droidun Python framework, we read all the entities on the screen, and then we can cleverly prompt the agents to run the phone without any interference from the user.
- then the user can choose which agent to run and let the agent automatically do the desired task.

- Right now, the model has to open the reel to judge what reaction to give, but we can improve it to judge the reel just based on the Instagram reel over and any text written on the reel cover
- but for that, we need an updated version of DroidRun, which can detect text on images. For now, it can only detect readable entities like text boxes and iamges but no text as an image
- Furthermore, we can improve its speed by using a more advanced AI and also engineering the prompt using CoT (chain of thinking) concepts to improve its performance and speed

## 📋 Prerequisites

- Python 3.8 or higher
- Android device with Instagram installed
- Droidrun setup configured
- Google Gemini API key

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DSK-champ/AI-Instagram-Agent
   cd Droidrun
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   
   **Get your API key from:** [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Configure Droidrun**
   
   Make sure Droidrun is properly configured and connected to your Android device. Refer to the [Droidrun documentation](https://droidrun.dev) for setup instructions.

## 💻 Usage

Run the main script:
```bash
python main.py
```

You'll be presented with a menu:
```
Available Agents:
  1. Reel Reactor - React to unread reels in Direct Messages
  2. Feed Customiser - Customize the explore feed based on interests
  3. Exit
```

### Using Reel Reactor
1. Select option `1`
2. The agent will automatically:
   - Open Instagram
   - Navigate to Direct Messages
   - Process all unread reels
   - React/reply based on content analysis

### Using Feed Customiser
1. Select option `2`
2. Enter your interests when prompted (comma-separated):
   ```
   Example: Educational, Funny, Marvel edits, Coding tips
   ```
3. The agent will:
   - Search for each interest category
   - Like 10 relevant posts/reels per category
   - Train your explore feed algorithm

## 📁 Project Structure

```
Droidrun/
├── main.py                 # Main entry point with menu
├── config.py               # Configuration management
├── reel_reactor.py         # Reel Reactor agent
├── feed_customiser.py      # Feed Customiser agent
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment file
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔧 Configuration

### API Key Management
The project uses environment variables for secure API key storage. Never commit your `.env` file to version control.

### Agent Settings
You can modify agent behavior in `config.py`:
- `max_steps`: Maximum steps the agent can take (default: 30 for Reel Reactor, 40 for Feed Customiser)
- `reasoning`: Enable Manager/Executor workflow (default: True)

## ⚠️ Important Notes

1. **API Key Security**: Never share or commit your API key. Always use environment variables.

2. **Device Connection**: Ensure your Android device is properly connected and Droidrun is configured before running the agents.

3. **Instagram Account**: Make sure you're logged into Instagram on your device.

4. **Rate Limiting**: Instagram may rate limit excessive automation. Use responsibly.

5. **Testing**: Test the agents in a controlled environment before using them extensively.

## 🐛 Troubleshooting

### API Key Error
```
ValueError: GEMINI_API_KEY environment variable not set
```
**Solution**: Make sure you've created a `.env` file with your API key.

### Droidrun Connection Error
**Solution**: Verify that:
- Your Android device is connected via USB/ADB
- Droidrun is properly installed and configured
- Instagram app is installed on the device

### Import Errors
**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📝 License

This project is created for hackathon purposes.

## 🤝 Contributing

This is a hackathon project. Contributions and improvements are welcome!

## 📧 Support

For issues related to:
- **Droidrun**: Check [Droidrun documentation](https://droidrun.dev)
- **Gemini API**: Check [Google AI documentation](https://ai.google.dev/docs)

---

**Built with ❤️ for the Hackathon**







