const quotes = {
  motivation: [
    { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
    { text: "Innovation distinguishes between a leader and a follower.", author: "Steve Jobs" },
    { text: "Stay hungry, stay foolish.", author: "Steve Jobs" },
    { text: "The best time to plant a tree was 20 years ago.", author: "Chinese Proverb" },
    { text: "Do what you can, with what you have, where you are.", author: "Theodore Roosevelt" },
  ],
  programming: [
    { text: "Code is like humor. When you have to explain it, it's bad.", author: "Cory House" },
    { text: "First, solve the problem. Then, write the code.", author: "John Johnson" },
    { text: "Simplicity is the soul of efficiency.", author: "Austin Freeman" },
    { text: "Make it work, make it right, make it fast.", author: "Kent Beck" },
  ],
};

function getRandomQuote(category) {
  const pool = category ? quotes[category] : Object.values(quotes).flat();
  return pool[Math.floor(Math.random() * pool.length)];
}

function displayQuote(category) {
  const q = getRandomQuote(category);
  console.log(`\n  "${q.text}"\n    — ${q.author}\n`);
}

module.exports = { getRandomQuote, displayQuote, quotes };

if (require.main === module) {
  const cat = process.argv[2];
  displayQuote(cat);
}
