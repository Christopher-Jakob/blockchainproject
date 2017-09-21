import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreaterecordComponent } from './createrecord.component';

describe('CreaterecordComponent', () => {
  let component: CreaterecordComponent;
  let fixture: ComponentFixture<CreaterecordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreaterecordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreaterecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
