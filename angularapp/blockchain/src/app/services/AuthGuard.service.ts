import{
  CanActivate,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
  Router,
  CanActivateChild}
  from '@angular/router';
import{Observable} from 'rxjs/Observable';
import{Injectable} from '@angular/core';

import {Authservice} from './services/auth.service' ;

@Injectable()
export class AuthGuard implements  canActivate, CanActivateChild{
  constructor(private authservice: Authservice, private router: Router){}

  canActivate(route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean{
    return this.authservice.isAuthenticated()
      .then(
        (authenticated: boolean)=>{
          if(authenticated) {
            return true;
          }
          else{
            this.router.navigate(['/']);
          }
        }
      );
  }
}

CanActivateChild(route: ActivatedRouteSnapshot,
                 state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean{
  return this.canActivate(route,state);
  }
}
