import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SigninpageComponent } from './signinpage/signinpage.component';
import { CreateviewrecordComponent } from './createviewrecord/createviewrecord.component';
import { CreaterecordComponent } from './createviewrecord/createrecord/createrecord.component';
import { ViewrecordComponent } from './createviewrecord/viewrecord/viewrecord.component';
import { NavbarComponent } from './navbar/navbar.component';


@NgModule({
  declarations: [
    AppComponent,
    SigninpageComponent,
    CreateviewrecordComponent,
    CreaterecordComponent,
    ViewrecordComponent,
    NavbarComponent,
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
