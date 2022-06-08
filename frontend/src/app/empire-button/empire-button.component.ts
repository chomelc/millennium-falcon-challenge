import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-empire-button',
  templateUrl: './empire-button.component.html',
  styleUrls: ['./empire-button.component.css'],
})
export class EmpireButtonComponent implements OnInit {
  label = '[empire file]';
  @Input()
  empireFile: string | ArrayBuffer | null | undefined;
  @Output() empireFileChange = new EventEmitter<
    string | ArrayBuffer | null | undefined
  >();

  upload(event: Event) {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0] as File;
    this.label = file.name;
    this.readFile(file);
  }

  readFile(file: File) {
    const reader = new FileReader();
    reader.addEventListener('load', (event) => {
      this.empireFile = event.target?.result;
      this.empireFileChange.emit(event.target?.result);
    });
    reader.readAsText(file);
  }

  clearFile() {
    let input = <HTMLInputElement>document.getElementById('empire');
    if (input) {
      input.value = '';
      this.empireFile = undefined;
      this.empireFileChange.emit(undefined);
      this.label = '[empire file]';
    }
  }

  constructor() {}

  ngOnInit(): void {}
}
