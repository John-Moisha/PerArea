"""{{ form.email|as_crispy_field }}-->"""



'''
Verif Template Html



<!--    <div class="row">-->
<!--        <div class="col-12 col-xl-12">-->
<!--            <div class="card card-body border-0 shadow mb-4">-->
<!--                <h2 class="h5 mb-4">Информация об аккаунте</h2>-->
<!--                <form method="post" enctype="multipart/form-data">-->
<!--                    {% csrf_token %}-->
<!--                    {{ form|as_crispy_errors }}-->
<!--                    <div class="row">-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <div>-->
<!--                                <label for="first_name">Имя</label>-->
<!--                                First_name-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <div>-->
<!--                                <label for="last_name">Фамилия</label>-->
<!--                                Last_name-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="row align-items-center">-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <label for="birthday">Дата рождения</label>-->
<!--                            <div class="input-group">-->
<!--                                <span class="input-group-text">-->
<!--                                    <svg class="icon icon-xs" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>-->
<!--                                </span>-->
<!--                                {{ form.date_of_birth|as_crispy_field }}-->
<!--&lt;!&ndash;                                <input data-datepicker="" class="form-control" id="birthday" type="text" placeholder="дд/мм/гггг" required>&ndash;&gt;-->
<!--                              </div>-->
<!--                        </div>-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <label for="sex">Пол</label>-->
<!--                            {{ form.sex|as_crispy_field }}-->
<!--&lt;!&ndash;                            {{ form.sex }}&ndash;&gt;-->
<!--&lt;!&ndash;                            {{ form.sex.errors }}&ndash;&gt;-->
<!--&lt;!&ndash;                            <select class="form-select mb-0" id="gender" aria-label="Gender select example">&ndash;&gt;-->
<!--&lt;!&ndash;                                <option selected>Сделайте свой выбор</option>&ndash;&gt;-->
<!--&lt;!&ndash;                                <option value="1">Женский</option>&ndash;&gt;-->
<!--&lt;!&ndash;                                <option value="2">Мужской</option>&ndash;&gt;-->
<!--&lt;!&ndash;                            </select>&ndash;&gt;-->
<!--                        </div>-->
<!--                    </div>-->

<!--                    <h2 class="h5 my-4">Адресс проживания</h2>-->
<!--                    <div class="row">-->
<!--                        <div class="col-sm-9 mb-3">-->
<!--                            <div class="form-group">-->
<!--                                    {{ form.street_line|as_crispy_field }}-->
<!--&lt;!&ndash;                                <input class="form-control" id="address" type="text" placeholder="Введите свой адрес" required>&ndash;&gt;-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-sm-3 mb-3">-->
<!--                            <div class="form-group">-->
<!--&lt;!&ndash;                                <label for="number">Номер</label>&ndash;&gt;-->
<!--                                {{ form.number|as_crispy_field }}-->
<!--&lt;!&ndash;                                <input class="form-control" id="number" type="number" placeholder="№" required>&ndash;&gt;-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="row">-->
<!--                        <div class="col-sm-4 mb-3">-->
<!--                            <div class="form-group">-->
<!--&lt;!&ndash;                                <label for="city">Город</label>&ndash;&gt;-->
<!--                                    {{ form.city|as_crispy_field }}-->
<!--&lt;!&ndash;                                <input class="form-control" id="city" type="text" placeholder="Город" required>&ndash;&gt;-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-sm-4 mb-3">-->
<!--&lt;!&ndash;                            <label for="state">Область</label>&ndash;&gt;-->
<!--                                {{ form.state|as_crispy_field }}-->
<!--                        </div>-->
<!--                        <div class="col-sm-4">-->
<!--                            <div class="form-group">-->
<!--&lt;!&ndash;                                <label for="zipcode">Индекс</label>&ndash;&gt;-->
<!--                                    {{ form.zipcode|as_crispy_field }}-->
<!--&lt;!&ndash;                                <input class="form-control" id="zip" type="tel" placeholder="Индекс" required>&ndash;&gt;-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="mt-3">-->
<!--                        <button class="btn btn-gray-800 mt-2 animate-up-2" type="submit">Сохранить</button>-->
<!--                    </div>-->

<!--                </form>-->
<!--            </div>-->


<!--        </div>-->

<!--    </div>-->


<!--    <div class="row">-->
<!--        <div class="col-12 col-xl-12">-->
<!--            <div class="card card-body border-0 shadow mb-4">-->
<!--                <h2 class="h5 mb-4">Информация об аккаунте</h2>-->


<!--                    <div class="row">-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <div>-->
<!--                                <label for="first_name">Имя</label>-->
<!--                                <input class="form-control" id="first_name" type="text" placeholder="Введите свое имя" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <div>-->
<!--                                <label for="last_name">Фамилия</label>-->
<!--                                <input class="form-control" id="last_name" type="text" placeholder="Введите свою фамилию" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="row align-items-center">-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <label for="birthday">Дата рождения</label>-->
<!--                            <div class="input-group">-->
<!--                                <span class="input-group-text">-->
<!--                                    <svg class="icon icon-xs" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>-->
<!--                                </span>-->
<!--                                <input data-datepicker="" class="form-control" id="birthday" type="text" placeholder="дд/мм/гггг" required>-->
<!--                              </div>-->
<!--                        </div>-->
<!--                        <div class="col-md-6 mb-3">-->
<!--                            <label for="gender">Пол</label>-->
<!--                            <select class="form-select mb-0" id="gender" aria-label="Gender select example">-->
<!--                                <option selected>Сделайте свой выбор</option>-->
<!--                                <option value="1">Женский</option>-->
<!--                                <option value="2">Мужской</option>-->
<!--                            </select>-->
<!--                        </div>-->
<!--                    </div>-->

<!--                    <h2 class="h5 my-4">Адресс проживания</h2>-->
<!--                    <div class="row">-->
<!--                        <div class="col-sm-9 mb-3">-->
<!--                            <div class="form-group">-->
<!--                                <label for="address">Адрес</label>-->
<!--                                <input class="form-control" id="address" type="text" placeholder="Введите свой адрес" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-sm-3 mb-3">-->
<!--                            <div class="form-group">-->
<!--                                <label for="number">Номер</label>-->
<!--                                <input class="form-control" id="number" type="number" placeholder="№" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="row">-->
<!--                        <div class="col-sm-4 mb-3">-->
<!--                            <div class="form-group">-->
<!--                                <label for="city">Город</label>-->
<!--                                <input class="form-control" id="city" type="text" placeholder="Город" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-sm-4 mb-3">-->
<!--                            <label for="state">Область</label>-->
<!--                            <select class="form-select w-100 mb-0" id="state" name="state" aria-label="State select example">-->
<!--                                <option selected>Сделайте свой выбор</option>-->
<!--                                <option value="AL">Alabama</option>-->
<!--                                <option value="AK">Alaska</option>-->
<!--                                <option value="AZ">Arizona</option>-->
<!--                                <option value="AR">Arkansas</option>-->
<!--                                <option value="CA">California</option>-->
<!--                                <option value="CO">Colorado</option>-->
<!--                                <option value="CT">Connecticut</option>-->
<!--                                <option value="DE">Delaware</option>-->
<!--                                <option value="DC">District Of Columbia</option>-->
<!--                                <option value="FL">Florida</option>-->
<!--                                <option value="GA">Georgia</option>-->
<!--                                <option value="HI">Hawaii</option>-->
<!--                                <option value="ID">Idaho</option>-->
<!--                                <option value="IL">Illinois</option>-->
<!--                                <option value="IN">Indiana</option>-->
<!--                                <option value="IA">Iowa</option>-->
<!--                                <option value="KS">Kansas</option>-->
<!--                                <option value="KY">Kentucky</option>-->
<!--                                <option value="LA">Louisiana</option>-->
<!--                                <option value="ME">Maine</option>-->
<!--                                <option value="MD">Maryland</option>-->
<!--                                <option value="MA">Massachusetts</option>-->
<!--                                <option value="MI">Michigan</option>-->
<!--                                <option value="MN">Minnesota</option>-->
<!--                                <option value="MS">Mississippi</option>-->
<!--                                <option value="MO">Missouri</option>-->
<!--                                <option value="MT">Montana</option>-->
<!--                                <option value="NE">Nebraska</option>-->
<!--                                <option value="NV">Nevada</option>-->
<!--                                <option value="NH">New Hampshire</option>-->
<!--                                <option value="NJ">New Jersey</option>-->
<!--                                <option value="NM">New Mexico</option>-->
<!--                                <option value="NY">New York</option>-->
<!--                                <option value="NC">North Carolina</option>-->
<!--                                <option value="ND">North Dakota</option>-->
<!--                                <option value="OH">Ohio</option>-->
<!--                                <option value="OK">Oklahoma</option>-->
<!--                                <option value="OR">Oregon</option>-->
<!--                                <option value="PA">Pennsylvania</option>-->
<!--                                <option value="RI">Rhode Island</option>-->
<!--                                <option value="SC">South Carolina</option>-->
<!--                                <option value="SD">South Dakota</option>-->
<!--                                <option value="TN">Tennessee</option>-->
<!--                                <option value="TX">Texas</option>-->
<!--                                <option value="UT">Utah</option>-->
<!--                                <option value="VT">Vermont</option>-->
<!--                                <option value="VA">Virginia</option>-->
<!--                                <option value="WA">Washington</option>-->
<!--                                <option value="WV">West Virginia</option>-->
<!--                                <option value="WI">Wisconsin</option>-->
<!--                                <option value="WY">Wyoming</option>-->
<!--                            </select>-->
<!--                        </div>-->
<!--                        <div class="col-sm-4">-->
<!--                            <div class="form-group">-->
<!--                                <label for="zip">Индекс</label>-->
<!--                                <input class="form-control" id="zip" type="tel" placeholder="Индекс" required>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="mt-3">-->
<!--                        <button class="btn btn-gray-800 mt-2 animate-up-2" type="submit">Сохранить</button>-->
<!--                    </div>-->

<!--            </div>-->


<!--        </div>-->

<!--    </div>-->
<!--    <div class="row border-0 mb-4">-->
<!--                <div class="col-6">-->
<!--                    <div class="card card-body border-0 shadow mb-4">-->
<!--                        <h2 class="h5 mb-4">Фото документа 1 стр.</h2>-->
<!--                        <div class="d-flex align-items-center">-->
<!--                            <div class="me-3">-->
<!--                                &lt;!&ndash; Avatar &ndash;&gt;-->
<!--                                <img class="rounded avatar-xl" src="{{ ASSETS_ROOT }}/img/team/profile-picture-3.jpg" alt="change avatar">-->
<!--                            </div>-->
<!--                            <div class="file-field">-->
<!--                                <div class="d-flex justify-content-xl-center ms-xl-3">-->
<!--                                    <div class="d-flex">-->
<!--                                        <svg class="icon text-gray-500 me-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z" clip-rule="evenodd"></path></svg>-->
<!--                                        <input type="file">-->
<!--                                        <div class="d-md-block text-left">-->
<!--                                            <div class="fw-normal text-dark mb-1">Choose Image</div>-->
<!--                                            <div class="text-gray small">JPG, GIF or PNG. Max size of 800K</div>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                              </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--                <div class="col-6">-->
<!--                    <div class="card card-body border-0 shadow">-->
<!--                        <h2 class="h5 mb-4">Фото документа 2 стр.</h2>-->
<!--                        <div class="d-flex align-items-center">-->
<!--                            <div class="me-3">-->
<!--                                &lt;!&ndash; Avatar &ndash;&gt;-->
<!--                                <img class="rounded avatar-xl" src="{{ ASSETS_ROOT }}/img/profile-cover.jpg" alt="change cover">-->
<!--                            </div>-->
<!--                            <div class="file-field">-->
<!--                                <div class="d-flex justify-content-xl-center ms-xl-3">-->
<!--                                    <div class="d-flex">-->
<!--                                        <svg class="icon text-gray-500 me-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z" clip-rule="evenodd"></path></svg>-->
<!--                                        <input type="file">-->
<!--                                        <div class="d-md-block text-left">-->
<!--                                            <div class="fw-normal text-dark mb-1">Choose Image</div>-->
<!--                                            <div class="text-gray small">JPG, GIF or PNG. Max size of 800K</div>-->
<!--                                        </div>-->
<!--                                    </div>-->
<!--                                </div>-->
<!--                              </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--            </div>-->



'''


'''
    <div class="row">
        <div class="col-12 col-xl-12">
            <div class="card card-body border-0 shadow mb-4">
                <h2 class="h5 mb-4">Информация об аккаунте</h2>
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}

                    {{ form.passport1|as_crispy_field }}

                <div class="mt-3">
                        <button class="btn btn-gray-800 mt-2 animate-up-2" type="submit">Сохранить</button>
                    </div>

                </form>


            </div>
        </div>
    </div>
'''


'''

<div class="row">
        <div class="col-12 col-xl-12">
            <div class="card card-body border-0 shadow mb-4">
                <h2 class="h5 mb-4">Информация об аккаунте</h2>
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form_errors }}
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div>
                                <label for="first_name">Имя</label>
                                First_name
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div>
                                <label for="last_name">Фамилия</label>
                                Last_name
                            </div>
                        </div>
                    </div>
                    <div class="row align-items-center">
                        <div class="col-md-6 mb-3">
                            <label for="birthday">Дата рождения</label>
                            <div class="input-group">
                                <span class="input-group-text">
                                    <svg class="icon icon-xs" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>
                                </span>
                                {{ form.date_of_birth|as_crispy_field }}{{ form.date_of_birth.errors }}
    <!--                                <input data-datepicker="" class="form-control" id="birthday" type="text" placeholder="дд/мм/гггг" required>-->
                              </div>
                        </div>
                        <div class="col-md-6 mb-3">
    
                            {{ form.sex|as_crispy_field }}{{ form.sex.errors }}
    <!--                            {{ form.sex }}-->
    <!--                            {{ form.sex.errors }}-->
    <!--                            <select class="form-select mb-0" id="gender" aria-label="Gender select example">-->
    <!--                                <option selected>Сделайте свой выбор</option>-->
    <!--                                <option value="1">Женский</option>-->
    <!--                                <option value="2">Мужской</option>-->
    <!--                            </select>-->
                        </div>
                    </div>
    
                    <h2 class="h5 my-4">Адресс проживания</h2>
                    <div class="row">
                        <div class="col-sm-9 mb-3">
                            <div class="form-group">
                                    {{ form.street_line|as_crispy_field }}{{ form.street_line.errors }}
    <!--                                <input class="form-control" id="address" type="text" placeholder="Введите свой адрес" required>-->
                            </div>
                        </div>
                        <div class="col-sm-3 mb-3">
                            <div class="form-group">
    <!--                                <label for="number">Номер</label>-->
                                {{ form.number|as_crispy_field }}{{ form.number.errors }}
    <!--                                <input class="form-control" id="number" type="number" placeholder="№" required>-->
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-4 mb-3">
                            <div class="form-group">
    <!--                                <label for="city">Город</label>-->
                                    {{ form.city|as_crispy_field }}{{ form.city.errors }}
    <!--                                <input class="form-control" id="city" type="text" placeholder="Город" required>-->
                            </div>
                        </div>
                        <div class="col-sm-4 mb-3">
    <!--                            <label for="state">Область</label>-->
                                {{ form.state|as_crispy_field }}{{ form.state.errors }}
                        </div>
                        <div class="col-sm-4">
                            <div class="form-group">
    <!--                                <label for="zipcode">Индекс</label>-->
                                    {{ form.zipcode|as_crispy_field }}{{ form.zipcode.errors }}
    <!--                                <input class="form-control" id="zip" type="tel" placeholder="Индекс" required>-->
                            </div>
                        </div>
                    </div>
                    <div class="mt-3">
                        <button class="btn btn-gray-800 mt-2 animate-up-2" type="submit">Сохранить</button>
                    </div>
    
                </form>
            </div>
    
    
        </div>

    </div>
    
    {{ form.zipcode|as_crispy_field }}
'''



'''
<div class="row">
        <div class="col-12 col-xl-12">
            <div class="card card-body border-0 shadow mb-4">
                <h2 class="h5 mb-4">Информация об аккаунте</h2>
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form.as_p}}




                <div class="mt-3">
                        <button class="btn btn-gray-800 mt-2 animate-up-2" type="submit">Сохранить</button>
                    </div>

                </form>


            </div>
        </div>
    </div>
    
    {{ form.city|as_crispy_field }}{{ form.city.errors }}
'''

'''
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div>
                                <label for="date_of_birth">{{ form.date_of_birth.label }}</label>
                                    {{ form.date_of_birth }}{{ form.date_of_birth.errors }}
                            </div>
                        </div>
                    </div>
'''