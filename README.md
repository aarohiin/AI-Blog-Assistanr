📝 NVIDIA Blog Generator
A simple, powerful Streamlit app that generates full-length blog posts using NVIDIA's LLaMA-3 based Nemotron-70B Instruct LLM — no API key hardcoded! Ideal for developers, marketers, and content creators who want quick, structured content with custom tone and audience options.

🚀 Features
🔒 Secure API Key integration using .env file

✍️ Supports multiple blog types: How-to, Listicle, Explainer, etc.

🎭 Custom tone: Professional, Casual, Witty, and more

🎯 Tailor-made for specific audiences like Developers or General Readers

📜 Download generated content as Markdown (.md)

⚡ Built with Streamlit for fast prototyping

🔧 Requirements
Install all dependencies using the included requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
Requirements:

nginx
Copy
Edit
streamlit
openai
python-dotenv
🔑 Get Your NVIDIA API Key
Visit: https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct

Sign in with your NVIDIA Developer account.

Generate your API Key and copy it.

⚙️ Setup & Run
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/nvidia-blog-generator.git
cd nvidia-blog-generator
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure the API key
Create a .env file in the root directory (or copy the example):

bash
Copy
Edit
cp .env.example .env
Then, add your key like so:

env
Copy
Edit
NVIDIA_API_KEY=your-nvidia-api-key-here
5. Run the app
bash
Copy
Edit
streamlit run app.py
📁 File Explanation
File	Purpose
app.py	Main Streamlit application that runs the blog generator
requirements.txt	List of dependencies needed for the app
.env.example	Template for the .env file (replace with your NVIDIA API Key)
README.md	Documentation for setup and usage
💡 Example Use Cases
Writing SEO-optimized blogs quickly

Automating internal documentation

Brainstorming content ideas

Personalized storytelling or product reviews

🛡️ Security Note
Your API key is never stored or shared. This app uses the python-dotenv package to read your API key locally from an environment file (.env).

📬 Contact
Feel free to open an issue or pull request for suggestions or improvements!
