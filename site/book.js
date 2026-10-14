// Style the book's Markdown conventions without changing the chapter files.
document.querySelectorAll(".content main p").forEach((p) => {
  const text = p.textContent.trim();
  if (text.startsWith("[Insert diagram:")) {
    p.className = "diagram-placeholder";
    p.textContent = "🖼 ছবি আসছে";
  } else if (p.children.length === 1 && p.firstElementChild.tagName === "STRONG" && text === "একটু ভাবো") {
    const box = document.createElement("div");
    box.className = "callout-think";
    p.before(box);
    const next = p.nextElementSibling;
    box.append(p);
    if (next && next.tagName === "P") box.append(next);
  }
});
