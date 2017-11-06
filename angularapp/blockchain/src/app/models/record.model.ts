/**
 * Created by rickus on 10/26/17.
 */

export class Record{
  public firstname: string;
  public lastname : string;
  public dob : string;
  public ssn: string;
  public allergies: string;
  public notes: string;

  constructor(firstname: string, lastname: string, dob: string, ssn: string,
  allergies: string, notes: string){
    this.firstname = firstname;
    this.lastname = lastname;
    this.dob = dob;
    this.ssn = ssn;
    this.allergies = allergies;
    this.notes = notes;
  }
}
