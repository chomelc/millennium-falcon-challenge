import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { OddsComponent } from './odds/odds.component';

const routes: Routes = [
  {
    // default route => /
    path: '',
    component: LandingPageComponent,
  },
  {
    path: 'odds',
    component: OddsComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
