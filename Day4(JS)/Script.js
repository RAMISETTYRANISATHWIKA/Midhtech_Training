let students=[];
function addStudent(){
    let name=document.getElementById("name").value;
    students.push(name);
    showStudents();
    document.getElementById("name").value = "";
}
function deleteStudent(index){
    students.splice(index, 1);
    showStudents();
}
function showStudents(){
    let output="";
    for(let i=0;i<students.length;i++){
        output += "<li>" + students[i] + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+ " <button onclick='deleteStudent(" + i + ")'>Delete</button>"+"</li>";
    }
    document.getElementById("list").innerHTML = output;
}