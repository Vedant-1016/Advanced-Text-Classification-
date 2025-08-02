<h1>🧠 Advanced Text Classification using spaCy</h1>

<p>This project explores <strong>Advanced Text Classification</strong> using the spaCy NLP library.</p>

<p>As a first step, I've implemented <strong>Named Entity Recognition (NER)</strong> to extract relevant entities from food-related text inputs. This NER system is designed as part of a <strong>food tracking bot</strong>, which will eventually be integrated into a larger personalized AI agent project (PIE).</p>

<h2>💡 What It Does</h2>

<ul>
  <li>Trains a custom spaCy model to recognize food-related entities:
    <ul>
      <li><code>QUANTITY_VALUE</code></li>
      <li><code>QUANTITY_UNIT</code></li>
      <li><code>FOOD_ITEM</code></li>
      <li><code>PORTION_SIZE</code></li>
    </ul>
  </li>
  <li>Handles entity alignment issues during training</li>
  <li>Saves and loads the model for prediction on new inputs</li>
</ul>

<h2>🔮 Example</h2>

<p><strong>Input:</strong><br>
<code>"I had 2 samosas and 1 cup of tea."</code></p>

<p><strong>Predicted Entities:</strong></p>
<ul>
  <li><code>2</code> → <code>QUANTITY_VALUE</code></li>
  <li><code>samosas</code> → <code>FOOD_ITEM</code></li>
  <li><code>1</code> → <code>QUANTITY_VALUE</code></li>
  <li><code>cup</code> → <code>QUANTITY_UNIT</code></li>
  <li><code>tea</code> → <code>FOOD_ITEM</code></li>
</ul>

<h2>📁 Project Structure</h2>

<pre><code>PIE_Food_NER/
├── calories.py           # Main script
├── train_data.json       # Training data (NER format)
├── food_ner_model/       # Trained model
├── requirements.txt      # Dependencies
├── .gitignore            # Ignore patterns
└── README.md             # Project description
</code></pre>

<h2>🛠️ Next Steps</h2>

<ul>
  <li>Add a chatbot interface using Streamlit</li>
  <li>Expand to calorie tracking and suggestion</li>
  <li>Add text classification for meal types (breakfast, dinner, etc.)</li>
</ul>

<hr>

<p>🚧 Work in Progress: First component of the PIE (Personalized AI Agent) Project</p>
