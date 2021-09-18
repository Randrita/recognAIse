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

var filesInput = document.getElementById("btn-0");
filesInput.addEventListener("change", function(event) {
    var files = event.target.files; //FileList object
    var output = document.getElementById("result");
    if (files.length > 0){
        form = filesInput.form;
        form.submit();
    }
});


// $('form').submit(function(e){
// 	// Stop the form submitting
//   	e.preventDefault();
//   	// Do whatever it is you wish to do
//   	//...
//   	// Now submit it 
//     // Don't use $(this).submit() FFS!
//   	// You'll never leave this function & smash the call stack! :D
//   	// e.currentTarget.submit();
//     return false;
// });
