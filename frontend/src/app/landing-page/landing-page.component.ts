import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css'],
})
export class LandingPageComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {}

  openModal() {
    var modal = document.getElementById('planets-map-modal');
    if (modal) {
      modal.style.display = 'block';
    }
  }
}
