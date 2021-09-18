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

function upload() {
    var filesInput = document.getElementById("btn-0");
    filesInput.addEventListener("change", function(event) {
        var files = event.target.files; //FileList object
        var output = document.getElementById("result");
        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            //Only pics
            if (!file.type.match('image'))
                continue;
            var picReader = new FileReader();
            picReader.addEventListener("load", function(event) {
                var picFile = event.target;
                var div = document.createElement("div");
                div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
                    "title='" + picFile.name + "'/>";
                output.insertBefore(div, null);
            });
            //Read the image
            picReader.readAsDataURL(file);
        }
    });

}

upload()