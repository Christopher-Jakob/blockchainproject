import { Component, OnInit, ViewChild } from '@angular/core';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-createrecord',
  templateUrl: './createrecord.component.html',
  styleUrls: ['./createrecord.component.css']
})
export class CreaterecordComponent implements OnInit {
  @ViewChild('f') createRecordForm : NgForm;
  submitted = false;
  record = {
    firstname: '',
    lastname: '',
    dob: '',
    ssn: '',
    allergies: '',
    notes: ''
  };

  constructor() { }

  ngOnInit() {

  }

  createRecord(){
   if(this.createRecordForm.valid){
     this.record.firstname = this.createRecordForm.value.firstname;
     this.record.lastname = this.createRecordForm.value.lastname;
     this.record.dob = this.createRecordForm.value.dob;
     this.record.ssn = this.createRecordForm.value.ssn;
     this.record.allergies = this.createRecordForm.value.allergies;
     this.record.notes = this.createRecordForm.value.notes;
     this.submitted = true;
   }


  }

}
