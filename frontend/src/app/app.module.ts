import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormComponent } from './form/form.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { EmpireButtonComponent } from './empire-button/empire-button.component';
import { OddsComponent } from './odds/odds.component';
import { ComputeOddsService } from './services/compute-odds.service';
import { HttpClientModule } from '@angular/common/http';
import { PlanetsMapModalComponent } from './planets-map-modal/planets-map-modal.component';
import { GetRoutesService } from './services/get-routes.service';

@NgModule({
  declarations: [
    AppComponent,
    FormComponent,
    LandingPageComponent,
    EmpireButtonComponent,
    OddsComponent,
    PlanetsMapModalComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule],
  providers: [ComputeOddsService, GetRoutesService],
  bootstrap: [AppComponent],
})
export class AppModule {}
