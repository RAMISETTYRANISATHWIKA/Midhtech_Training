class Student {
    constructor(id, name, marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }
    getGrade() {
        if (this.marks >= 90) {
            return "Grade A";
        } else if (this.marks >= 75) {
            return "Grade B";
        } else if (this.marks >= 60) {
            return "Grade C";
        } else {
            return "Fail";
        }
    }
    isPassed() {
        return this.marks >= 60;
    }
}
let students = [];
function addStudent(id, name, marks) {
    students.push(new Student(id, name, marks));
}
addStudent(101, "Rahul", 95);
addStudent(102, "Priya", 82);
addStudent(103, "Kiran", 67);
addStudent(104, "Suresh", 45);
addStudent(105, "Anitha", 91);
function displayStudents() {
    console.log("----- STUDENT REPORT -----\n");
    for (let student of students) {
        console.log(
            `ID: ${student.id} | ${student.name} | ${student.marks} | ${student.getGrade()}`
        );
    }
}
function findTopper() {
    return students.reduce((topper, student) =>
        student.marks > topper.marks ? student : topper
    );
}
function passedStudents() {
    return students.filter(student => student.isPassed());
}
function failedStudents() {
    return students.filter(student => !student.isPassed());
}
function averageMarks() {
    let total = students.reduce((sum, student) => sum + student.marks, 0);
    return total / students.length;
}
function searchById(id) {
    return students.find(student => student.id === id);
}
function searchByName(name) {
    return students.find(
        student => student.name.toLowerCase() === name.toLowerCase()
    );
}
function sortByMarks() {
    return [...students].sort((a, b) => b.marks - a.marks);
}
function topThreeStudents() {
    return sortByMarks().slice(0, 3);
}
displayStudents();
let topper = findTopper();
console.log("\nTopper:", topper.name, `(${topper.marks})`);
console.log("\nPassed Students:");
passedStudents().map(student => console.log(student.name));
console.log("\nFailed Students:");
failedStudents().map(student => console.log(student.name));
console.log("\nAverage Marks:", averageMarks());
console.log("\nTotal Passed:", passedStudents().length);
console.log("Total Failed:", failedStudents().length);
console.log("\nSearch By ID (103):");
let studentById = searchById(103);
console.log(
    `ID: ${studentById.id} | ${studentById.name} | ${studentById.marks} | ${studentById.getGrade()}`
);
console.log("\nSearch By Name (Priya):");
let studentByName = searchByName("Priya");
console.log(
    `ID: ${studentByName.id} | ${studentByName.name} | ${studentByName.marks} | ${studentByName.getGrade()}`
);
console.log("\nStudents Sorted by Marks (Descending):");
sortByMarks().forEach(student => {
    console.log(
        `${student.name} - ${student.marks} - ${student.getGrade()}`
    );
});
console.log("\nTop 3 Students:");
topThreeStudents().forEach((student, index) => {
    console.log(
        `${index + 1}. ${student.name} - ${student.marks} - ${student.getGrade()}`
    );
});