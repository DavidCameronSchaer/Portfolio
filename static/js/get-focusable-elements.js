/**
 * Returns back a NodeList of focusable elements
 * that exist within the passed parnt HTMLElement
 *
 * @param {HTMLElement} parent HTML element
 * @returns {NodeList} The focusable elements that we can find
 */
export default parent => {
  if (!parent) {
    console.warn("You need to pass a parent HTMLElement")
    return []
  }

  return parent.querySelectorAll(
    'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"]):not([disabled]), details:not([disabled]), summary:not(:disabled)'
  )
}

document.addEventListener("DOMContentLoaded", function () {
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var progressBar = entry.target.querySelector(".skill-progress")
        progressBar.style.width =
          progressBar.getAttribute("data-skill-level") + "%"
      } else {
        var progressBar = entry.target.querySelector(".skill-progress")
        progressBar.style.width = 0
      }
    })
  })

  document.querySelectorAll(".skill-bar").forEach(function (skillBar) {
    observer.observe(skillBar)
  })
})
