import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewrecordComponent } from './viewrecord.component';

describe('ViewrecordComponent', () => {
  let component: ViewrecordComponent;
  let fixture: ComponentFixture<ViewrecordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewrecordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewrecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
