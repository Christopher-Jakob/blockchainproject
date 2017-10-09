import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditrecordComponent } from './editrecord.component';

describe('EditrecordComponent', () => {
  let component: EditrecordComponent;
  let fixture: ComponentFixture<EditrecordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditrecordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditrecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
