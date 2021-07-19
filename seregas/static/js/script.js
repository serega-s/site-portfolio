console.log('Working')


let theme = localStorage.getItem('theme')

if (theme == null) {
  setTheme('blue')
} else {
  setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (let i = 0; themeDots.length > i; i++) {
  themeDots[i].addEventListener('click', function() {
    let mode = this.dataset.mode
    console.log('Option clicked', mode)
    setTheme(mode)
  })
}

function setTheme(mode) {
  if (mode == 'light') {
    document.getElementById('theme-style').href = static + '/default.css'
    localStorage.setItem('theme', mode)
  }
  if (mode == 'blue') {
    document.getElementById('theme-style').href = static + '/blue.css'
    localStorage.setItem('theme', mode)
  }
  if (mode == 'green') {
    document.getElementById('theme-style').href = static + '/green.css'
    localStorage.setItem('theme', mode)
  }
  if (mode == 'purple') {
    document.getElementById('theme-style').href = static + '/purple.css'
    localStorage.setItem('theme', mode)
  }

  localStorage.setItem('theme', mode)
}