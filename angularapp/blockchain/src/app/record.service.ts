/**
 * Created by rickus on 10/26/17.
 */

import {Record} from './models/record.model';
import {Http} from '@angular/http';
import {Injectable} from '@angular/core';
/*
public firstname: string;
public lastname : string;
public dob : string;
public ssn: string;
public allergies: string;
public notes: string;
*/

@Injectable()
export class RecordService{
  constructor(private http: Http){}
  giverecord: Record;
  gotrecords: Record[];

/* prepares a record from the submitted  form*/
addrecord(firstname: string, lastname: string, dob: string, ssn: string,
          allergies: string, notes: string){
  this.giverecord= new Record(firstname, lastname, dob, ssn, allergies, notes);
  }

  /* sends record to honeybager blockchain nodes*/
  sendrecord(record: Record){
    console.log(this.giverecord);
    return this.http.post('http://127.0.0.1:5000/addRecord' , this.giverecord);

  }

  getAllRecords(){
    return this.http.get('http://127.0.0.1:5000/getAllRecords');

  }

  setrecords(record: Record[]){
    this.gotrecords = record;
  }

  getrecords(){
    return this.gotrecords;
  }

  getrecordbyfirstlast(firstname: string, lastname: string){

    return this.http.get('http://127.0.0.1:5000/getByName?FirstName=' + firstname + '&LastName=' + lastname);
  }

  getrecordbyssn(ssn: string){

    return this.http.get('http://127.0.0.1:5000/getBySSN?SSN=' + ssn);
  }
}

