import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SigninpageComponent } from './signinpage.component';

describe('SigninpageComponent', () => {
  let component: SigninpageComponent;
  let fixture: ComponentFixture<SigninpageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SigninpageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SigninpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
