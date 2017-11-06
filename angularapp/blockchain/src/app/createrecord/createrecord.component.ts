import { Component, OnInit, ViewChild } from '@angular/core';
import {NgForm} from '@angular/forms';
import {RecordService} from "../record.service";

@Component({
  selector: 'app-createrecord',
  templateUrl: './createrecord.component.html',
  styleUrls: ['./createrecord.component.css']
})
export class CreaterecordComponent implements OnInit {
  @ViewChild('f') createRecordForm : NgForm;
  submitted = false;
  record = {
    FirstName: '',
    LastName: '',
    DOB: '',
    SSN: '',
    allergies: '',
    notes: ''
  };

  constructor(private recordservice: RecordService) { }

  ngOnInit() {

  }

  createRecord(){
   if(this.createRecordForm.valid){
     this.record.FirstName = this.createRecordForm.value.firstname;
     this.record.LastName = this.createRecordForm.value.lastname;
     this.record.DOB = this.createRecordForm.value.dob;
     this.record.SSN = this.createRecordForm.value.ssn;
     this.record.allergies = this.createRecordForm.value.allergies;
     this.record.notes = this.createRecordForm.value.notes;
     this.submitted = true;

     /* create a new record, and package for post request in variable giverecord */
     this.recordservice.addrecord(this.record.FirstName, this.record.LastName, this.record.DOB,
     this.record.SSN, this.record.allergies, this.record.notes);

     /* sends record to block chain */
     this.recordservice.sendrecord(this.recordservice.giverecord)
       .subscribe(
         (response) => console.log(response),
         (error) => console.log(error)
       );

   }


  }

}
