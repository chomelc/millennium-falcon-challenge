import { Component, OnInit } from '@angular/core';
import { GetRoutesService } from '../services/get-routes.service';

@Component({
  selector: 'app-planets-map-modal',
  templateUrl: './planets-map-modal.component.html',
  styleUrls: ['./planets-map-modal.component.css'],
})
export class PlanetsMapModalComponent implements OnInit {
  constructor(private getRoutesService: GetRoutesService) {}
  routes: any;

  ngOnInit(): void {
    this.getRoutes();
  }

  getRoutes(): void {
    this.getRoutesService.getRoutes().subscribe((data: any) => {
      this.routes = data;
    });
  }

  closeModal() {
    var modal = document.getElementById('planets-map-modal');
    if (modal) {
      modal.style.display = 'none';
    }
  }
}
