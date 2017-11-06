import {Component, OnInit, ViewChild} from '@angular/core';
import {RecordService} from '../record.service';
import {Record} from '../models/record.model';
import {Response} from '@angular/http';
import {NgForm} from "@angular/forms";

@Component({
  selector: 'app-browserecords',
  templateUrl: './browserecords.component.html',
  styleUrls: ['./browserecords.component.css']
})
export class BrowserecordsComponent implements OnInit{
  @ViewChild('fl')firstlastForm : NgForm;
  @ViewChild('ssn')ssnForm : NgForm;
  firstname = '';
  lastname = '';
  ssn = '';
  showrecords: Record[];



  constructor(private recordservice: RecordService) { }

  ngOnInit() {
  }

  getallrecords(){
    this.recordservice.getAllRecords()
      .subscribe(
        (response: Response)=>{
          const records: Record[]  = response.json();
          this.recordservice.setrecords(records);
          this.showrecords = this.recordservice.getrecords();
        }

        );


}

  firstlastsearch(){
    this.firstname = this.firstlastForm.value.firstname;
    this.lastname = this.firstlastForm.value.lastname;
    this.recordservice.getrecordbyfirstlast(this.firstname, this.lastname)
      .subscribe(
        (response: Response) =>{
      const records: Record[] = response.json();
      this.recordservice.setrecords(records);
      console.log(records);
    }
      );
  }

  ssnsearch(){
    this.ssn = this.ssnForm.value.ssn;
    this.recordservice.getrecordbyssn(this.ssn)
      .subscribe(
        (response: Response)=>{
          console.log(response);
          const records: Record[] = response.json();
          this.recordservice.setrecords(records);
          console.log(records);
        }
      );
  }





}
