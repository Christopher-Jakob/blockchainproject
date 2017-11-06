import { BrowserModule } from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { CreaterecordComponent } from './createrecord/createrecord.component';
import { NavbarComponent } from './navbar/navbar.component';
import {HttpModule} from '@angular/http';
import {RecordService} from './record.service';
import { BrowserecordsComponent } from './browserecords/browserecords.component';
import { SigninComponent } from './signin/signin.component';
import {RouterModule, Routes} from "@angular/router";

const appRoutes: Routes = [
  {path: '', component: SigninComponent},
  {path: 'create', component: CreaterecordComponent},
  {path: 'browse', component: BrowserecordsComponent}

];


@NgModule({
  declarations: [
    AppComponent,
    CreaterecordComponent,
    NavbarComponent,
    BrowserecordsComponent,
    SigninComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes),
  ],
  providers: [RecordService],
  bootstrap: [AppComponent]
})
export class AppModule { }
