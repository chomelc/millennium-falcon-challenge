import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ComputeOddsService } from '../services/compute-odds.service';

@Component({
  selector: 'app-odds',
  templateUrl: './odds.component.html',
  styleUrls: ['./odds.component.css'],
})
export class OddsComponent implements OnInit {
  odds: number = 0;
  path: string = '';
  total_travel_time: number = 0;
  empire_file_location: string | undefined;

  constructor(
    private route: ActivatedRoute,
    private computeOddsService: ComputeOddsService
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.empire_file_location = params['empire'];
    });
    this.computeOdds();
  }

  computeOdds(): void {
    if (this.empire_file_location) {
      this.computeOddsService
        .computeOdds(this.empire_file_location)
        .subscribe((data: any) => {
          this.odds = data.odds;
          this.path = this.formatPath(data.path);
          this.total_travel_time = data.total_travel_time;
        });
    }
  }

  formatPath(path: string): string {
    // removing square brackets
    let new_path = path.slice(1, -1);
    // removing single quotes
    new_path = new_path.replace(/['"]+/g, '');
    // removing "Bis" substring
    new_path = new_path.replace(/Bis/g, '');

    // constructing the final string
    let path_array = new_path.split(',');
    return path_array.join(' -> ');
  }
}
