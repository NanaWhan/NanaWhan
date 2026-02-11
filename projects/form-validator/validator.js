const validators = {
  required: (value) => value !== null && value !== undefined && value.toString().trim() !== '',
  email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
  minLength: (min) => (value) => value && value.length >= min,
  maxLength: (max) => (value) => value && value.length <= max,
  pattern: (regex) => (value) => new RegExp(regex).test(value),
  numeric: (value) => !isNaN(parseFloat(value)) && isFinite(value),
  url: (value) => {
    try { new URL(value); return true; } catch { return false; }
  }
};

function validate(data, rules) {
  const errors = {};
  for (const [field, fieldRules] of Object.entries(rules)) {
    const value = data[field];
    const fieldErrors = [];
    for (const rule of fieldRules) {
      if (typeof rule === 'string') {
        if (!validators[rule](value)) {
          fieldErrors.push(`${field} failed ${rule} validation`);
        }
      } else if (typeof rule === 'object') {
        const [name, param] = Object.entries(rule)[0];
        if (!validators[name](param)(value)) {
          fieldErrors.push(`${field} failed ${name}(${param}) validation`);
        }
      }
    }
    if (fieldErrors.length > 0) errors[field] = fieldErrors;
  }
  return { valid: Object.keys(errors).length === 0, errors };
}

module.exports = { validate, validators };
