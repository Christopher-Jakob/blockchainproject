import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

import{SigninpageComponent} from './signinpage/signinpage.component';
import{ViewrecordComponent} from './createviewrecord/viewrecord/ViewrecordComponent';
import{CreaterecordComponent} from './createviewrecord/createrecord/createrecord.component';
import {EditrecordComponent} from './createviewrecord/editrecord/editrecord.component';
import {PagenotfoundComponent} from './pagenotfound/pagenotfound.component'
import {AuthGuard} from './services/auth-guard.service';
import {CanDeactivateGuard} from './services/canDeactivateGuard.service';


const appRoutes: Routes = [
  {path: '', component: SigninpageComponent},
  {path: 'view:id',
    canActivateChild:[AuthGuard],
    component: ViewrecordComponent,
    children: [ {
    path: ':id/edit', component: EditrecordComponent,
    canDeactivate: [canDeactivateGuard] }
  ]  },
  {path: 'create', canActivate:[AuthGuard], canDeactivate:[canDeactivateGuard], component: CreaterecordComponent},
  {path: 'not-found', component: PagenotfoundComponent},
  {path: '**', redirectTo: '/not-found'}
  ];

@NgModule({
  imports:[
    RouterModule.forRoot(appRoutes)],
  exports[RouterModule]

})
export class AppRoutingModule{

}



