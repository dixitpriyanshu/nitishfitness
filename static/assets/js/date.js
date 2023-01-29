const today = new Date();

const dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear() - 16;

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
    
const date = yyyy + '-' + mm + '-' + dd;
document.getElementById("dob").setAttribute('max', date);