const { test } = require("node:test");
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");
const vm = require("node:vm");

test("clock shows actual IST, advances, and refreshes after a hidden tab", () => {
  let now = new Date("2026-09-29T20:45:59Z");
  const nodes = Object.fromEntries(["india-clock", "clock-date", "year"].map(id => [id, {}]));
  let tick, visibility;
  const document = { hidden: false, getElementById: id => nodes[id], addEventListener: (_, fn) => { visibility = fn; } };
  class TestDate extends Date { constructor() { super(now); } }
  vm.runInNewContext(readFileSync(join(__dirname, "../site.js"), "utf8"), {
    Date: TestDate, Intl, document, window: { setInterval: (fn, ms) => { assert.equal(ms, 1000); tick = fn; } },
  });
  assert.equal(nodes["india-clock"].textContent, "02:15:59");
  assert.equal(nodes["india-clock"].dateTime, now.toISOString());
  assert.match(nodes["clock-date"].textContent, /30 Sept 2026/);
  now = new Date("2026-09-29T20:46:00Z"); tick();
  assert.equal(nodes["india-clock"].textContent, "02:16:00");
  document.hidden = true;
  now = new Date("2026-09-30T00:00:00Z"); tick();
  assert.equal(nodes["india-clock"].textContent, "02:16:00");
  document.hidden = false; visibility();
  assert.equal(nodes["india-clock"].textContent, "05:30:00");
});
