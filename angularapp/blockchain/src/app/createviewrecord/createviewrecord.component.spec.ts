import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateviewrecordComponent } from './createviewrecord.component';

describe('CreateviewrecordComponent', () => {
  let component: CreateviewrecordComponent;
  let fixture: ComponentFixture<CreateviewrecordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateviewrecordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateviewrecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
