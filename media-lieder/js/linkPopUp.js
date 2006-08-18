function popUpWin( ) {
    window.open(this.href, 'newwin', 'width=600,height=600');
    return false;
}

function makeLinkPopUp (pattern) {
    if (!document.getElementById) return
    
    var elements = document.getElementsBySelector (pattern) ;
    for (var i = 0; i < elements.length; i++) {
            elements[i].onclick = popUpWin ;
    }
}

var pattern = '#article-la-premsa-ha-dit-list h2 a' ;
var run_onload = function () { makeLinkPopUp (pattern); }
window.onload = run_onload ;
