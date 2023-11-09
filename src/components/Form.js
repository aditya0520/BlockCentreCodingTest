import { Component } from "react";
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'
import APIService from "./APIService";
import moment from 'moment';

class Form extends Component {
    date = null;
    state = {
        firstname: "",
        lastname: "",
        gender: "",
        dob: (new Date()).toLocaleDateString,
        email: "",
    };
    handleChange = (event) => {
        if (event.target.id === "firstName") {
            this.setState({
                firstname: event.target.value,
            });
        }
        if (event.target.id === "lastName") {
            this.setState({
                lastname: event.target.value,
            });
        }
        if (event.target.id === "email") {
            this.setState({
                email: event.target.value,
            });
        }
    };
    handleOptionChange = (event) => {
        this.setState({
            gender: event.target.value,
        });
        console.log(this.state.gender);
    }; 
    setDate = (event) => {
        var responseDate = moment(event).format("yyyy/MM/DD");
        this.setState({
            dob: responseDate.toString()
        });
        this.date = event
        console.log(this.state.dob);
    }; 
    insertArticle = (state) =>{
        APIService.InsertArticle({state})
        .then((response) => this.insertedArticle(response))
        .catch(error => console.log('error',error))
      }
    handleSubmit = (event) => {
        alert('Form submitted! ' + 'Email sent to ' + this.state.email);
        event.preventDefault()
        let fname = this.state.firstname
        let lname = this.state.lastname
        let dob = this.state.dob
        let gender = this.state.gender
        let email = this.state.email
        this.insertArticle({fname,lname,dob,gender,email})

    };
    render() {
        return (<div><h1>Form</h1>
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="firstName">First name:</label>
                <input onChange={this.handleChange} type="text" value={this.state.firstname} id="firstName"></input><br></br><br></br>
                <label htmlFor="lastName">Last name:</label>
                <input onChange={this.handleChange} type="text" value={this.state.lastname} id="lastName"></input><br></br><br></br>
                <h3>Select Gender</h3>
                <input onChange={this.handleOptionChange} type="radio" name="gender" value="Male" id="male" />
                <label htmlFor="male">Male</label>
                <input onChange={this.handleOptionChange} type="radio" name="gender" value="Female" id="female" />
                <label htmlFor="female">Female</label><br></br><br></br>
                <label htmlFor="dob">Date of Birth:</label><br></br>
                <DatePicker 
                selected={this.date}
                onChange={this.setDate}
                dateFormat="yyyy/MM/dd"
                minDate={new Date("1900/01/01")}
                maxDate={new Date()}
                isClearable
                showYearDropdown
                scrollableMonthYearDropdown
                /><br></br><br></br>
                <label htmlFor="email">Email:</label>
                <input onChange={this.handleChange} type="text" value={this.state.email} id="email"></input><br></br><br></br>
                <button type="submit">Submit</button>
            </form>
        </div>)
    }
}

export default Form;