function calculateBMI(weight, height, unit = 'metric') {
  let bmi;
  if (unit === 'metric') {
    bmi = weight / (height * height);
  } else {
    bmi = (703 * weight) / (height * height);
  }
  return Math.round(bmi * 10) / 10;
}

function getCategory(bmi) {
  if (bmi < 18.5) return 'Underweight';
  if (bmi < 25) return 'Normal weight';
  if (bmi < 30) return 'Overweight';
  return 'Obese';
}

function getReport(weight, height, unit = 'metric') {
  const bmi = calculateBMI(weight, height, unit);
  return {
    bmi,
    category: getCategory(bmi),
    healthy_range: { min: 18.5, max: 24.9 }
  };
}

module.exports = { calculateBMI, getCategory, getReport };
