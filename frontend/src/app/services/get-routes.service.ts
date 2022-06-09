import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class GetRoutesService {
  constructor(private http: HttpClient) {}

  public getRoutes() {
    const url: string = 'http://127.0.0.1:5000/routes';

    // execute request
    return this.http.get(url).pipe(
      catchError((err) => {
        throw new Error(err.message);
      })
    );
  }
}
