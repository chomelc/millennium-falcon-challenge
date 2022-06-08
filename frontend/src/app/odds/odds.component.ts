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
        });
    }
  }
}
