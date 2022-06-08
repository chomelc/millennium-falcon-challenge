import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
})
export class FormComponent implements OnInit {
  empireFile: string | ArrayBuffer | null | undefined;
  constructor() {}

  ngOnInit(): void {}
}
