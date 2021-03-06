import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {

  admin: boolean;

  constructor(private route: ActivatedRoute, private location: Location,
    private service: AuthService) { }

  ngOnInit() {

    this.getAdmin();
    // this.updateContadorUp();
  }

  ngOnChanges() {
    this.getAdmin();
    // this.updateContadorUp();
  }
  getAdmin(): void {
    const adm = this.route.snapshot.paramMap.get('adm');
    if (adm == 'true') {
      this.admin = true;
    } else {
      this.admin = false;
    }
  }

  //PESSOA AULA POST
  // updateContadorUp(): void {
  //   let relation = {
  //     Pessoas: 1,
  //     Aulas: 1,
  //     Contador: 1
  //   }
  //   this.service.updateCurrentAttendance(6, relation).subscribe(count => {
  //     console.log("FIZ REQUEST")
  //     console.log(count);
  //   })
  // }

}

