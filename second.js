function addClass(component, className) {
    var e = document.getElementById(component);
    e.removeAttribute('class');
    e.classList.add(className);
};

function setAnim(e) {
    var btn = document.getElementsByTagName('button')
    for (i = 0; i < btn.length; i++) {
        btn[i].classList.remove('active');
    }
    e.classList.toggle('active');
    value = e.innerText;
    addClass('component', value);
}

// first transition by default
var btn = document.getElementsByTagName('button')
btn[1].classList.add('active')
value = btn[1].innerText;
addClass('component', value);