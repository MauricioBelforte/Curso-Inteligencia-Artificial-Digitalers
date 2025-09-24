const dividir = require("./division");

test("División correcta", () => {
  expect(dividir(10, 2)).toBe(5);
});

test("División por cero lanza error", () => {
  expect(() => dividir(10, 0)).toThrow("División por cero");
});