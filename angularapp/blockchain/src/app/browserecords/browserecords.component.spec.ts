import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BrowserecordsComponent } from './browserecords.component';

describe('BrowserecordsComponent', () => {
  let component: BrowserecordsComponent;
  let fixture: ComponentFixture<BrowserecordsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BrowserecordsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BrowserecordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
