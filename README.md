# 🌍 Global Air Quality AI Agent

An interactive, LLM-powered conversational agent that retrieves, processes, and analyzes global air pollution data in real-time. 

This project utilizes a **Two-Phase Architecture**, separating the natural language processing (NLP) and data-fetching engine from the complex data visualizations. The conversational interface is built with Streamlit and Google's Gemini API, while the heavy Matplotlib visualizations are hosted in a dedicated Google Colab environment.

## 🏗️ Project Architecture
1. **The AI Brain (`agent` & `tools.py`):** Uses Google's Gemini 2.5 Flash model equipped with Python Function Calling. The LLM translates user questions into strict data queries, which are executed by a custom Pandas data engine to extract insights from a massive air quality CSV.
2. **The Web Interface (`app.py`):** A sleek, memory-persistent chat interface built with Streamlit that allows users to converse naturally with the dataset.
3. **The Visualization Engine (Google Colab):** Advanced Matplotlib horizontal and grouped bar charts for deep-dive visual analysis.

---

## 🚀 Live Demo & Visualizations
* **Interactive Data Visualizations (Phase 2):** [Insert your Google Colab Link Here]

---

## 💻 Tech Stack
* **Language:** Python 3
* **LLM / API:** Google GenAI SDK (Gemini 2.5 Flash)
* **Frontend:** Streamlit
* **Data Processing:** Pandas
* **Visualizations:** Matplotlib & NumPy (via Colab)

---

## 🛠️ Local Installation & Setup
Follow these steps to run the Streamlit AI Assistant on your local machine.

### 1. Clone the Repository
Download the project files to your local machine:
```bash
git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repo-Name].git
cd [Your-Repo-Name]
```
### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to keep dependencies clean.

* **Mac/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
* **Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

### 3. Install Dependencies
With your virtual environment activated, install the required Python libraries:

```bash
pip install -r requirements.txt
```
*(Note: If you do not have a `requirements.txt` file, run: `pip install pandas streamlit google-genai python-dotenv`)*

### 4. Configure Your API Key
This project requires a free Google Gemini API key.

1. Get an API key from [Google AI Studio](https://aistudio.google.com/).
2. Create a new file in the root directory of this project named exactly `.env`.
3. Add your API key to the file like this:

   ```text
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 5. Run the Application
Start the Streamlit local server:

```bash
streamlit run app.py
```
A browser window will automatically open to `http://localhost:8501` where you can start chatting with the agent!

## 💡 Example Prompts to Try
Once the app is running, try asking the AI:
* *"What is the current air quality and pollutant profile for Tokyo?"*
* *"Can you compare the air quality between London and Delhi?"*
* *"What are the top 5 most polluted cities in Vietnam?"*
