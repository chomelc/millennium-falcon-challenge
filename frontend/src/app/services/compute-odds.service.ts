import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ComputeOddsService {
  constructor(private http: HttpClient) {}

  public computeOdds(empire_file_location: string) {
    const url: string = `http://127.0.0.1:5000/give-me-the-odds?empire=${empire_file_location}`;

    // execute request
    return this.http.get(url).pipe(
      catchError((err) => {
        throw new Error(err.message);
      })
    );
  }
}
